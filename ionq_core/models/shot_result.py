# SPDX-FileCopyrightText: 2026 IonQ, Inc.
# SPDX-License-Identifier: Apache-2.0
# @generated

from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.shot_registers import ShotRegisters





T = TypeVar("T", bound="ShotResult")



@_attrs_define
class ShotResult:
    """ Result of a single shot — measured bit arrays for every named register.

        Attributes:
            registers (ShotRegisters): Per-register bit arrays for one shot, keyed by register name.
            leakage_bits (list[float] | Unset): Leakage for this shot, one 0 or 1 per executed qubit with 1 where the qubit
                leaked. Empty for a clean shot; any non-empty array marks the shot as leaked.
     """

    registers: ShotRegisters
    leakage_bits: list[float] | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.shot_registers import ShotRegisters
        registers = self.registers.to_dict()

        leakage_bits: list[float] | Unset = UNSET
        if not isinstance(self.leakage_bits, Unset):
            leakage_bits = self.leakage_bits




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "registers": registers,
        })
        if leakage_bits is not UNSET:
            field_dict["leakage_bits"] = leakage_bits

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.shot_registers import ShotRegisters
        d = dict(src_dict)
        registers = ShotRegisters.from_dict(d.pop("registers"))




        leakage_bits = cast(list[float], d.pop("leakage_bits", UNSET))


        shot_result = cls(
            registers=registers,
            leakage_bits=leakage_bits,
        )

        return shot_result

