# cloud-pact contracts action

Dispatches a contracts receiver workflow hosted in `ionq/pact` for a commit of the
calling repo, finds the resulting run by a correlation key, polls it, and ends with the same
verdict. Every wait takes an explicit bound, so the step fails cleanly instead of hanging
when the remote run never starts or never finishes.

The action only talks to the GitHub Actions API. Auth comes from the caller, normally an
[octo-sts](https://github.com/octo-sts/action) token whose trust policy in the target repo
grants `actions: write` to the calling workflow.

```yaml
permissions:
  id-token: write # federate to octo-sts

steps:
  - name: Get a token for cloud-pact Actions
    id: sts
    uses: octo-sts/action@f603d3be9d8dd9871a265776e625a27b00effe05 # v1.1.1
    with:
      domain: octo-sts.gh.ionq.co
      scope: ionq/pact
      identity: ionq-core-pact

  - uses: $/.github/actions/cloud-pact-contracts # other repos: ionq/ionq-core/.github/actions/cloud-pact-contracts@<sha>
    with:
      token: ${{ steps.sts.outputs.token }}
```

One receiver workflow exists per call type and `workflow:` picks it — the default checks a
commit on PRs and pushes; release jobs pass the release receiver plus its tag:

```yaml
      workflow: consumer-can-i-release.yaml # or consumer-record-release.yaml
      release-tag: ${{ github.ref_name }}
```

The receivers are shared across consumer repos: `consumer` selects the suite on the other
end and defaults to the calling repo's name. `sha`, `branch`, and `run-key` default to the
triggering event's values; `branch` resolves to empty on tag pushes and empty optional
inputs are not sent, since each receiver declares only the inputs it uses. Another repo
whose checks run in cloud-pact pins this action by commit SHA and needs no `workflow:`
override at all.

Await conditions: `start-timeout-seconds` (remote run must appear), `wait-timeout-seconds`
(run must complete; conclusion becomes `timed_out` otherwise), `poll-interval-seconds`, and
`success-conclusions` (default `success,skipped` — a skipped remote run counts as a pass).
Outputs `run-id`, `run-url`, and `conclusion` are set as soon as they are known, so an
advisory caller (`continue-on-error: true`) can still link the remote run on failure.
