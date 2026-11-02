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
  from ..models.json_object import JsonObject





T = TypeVar("T", bound="CircuitJobErrorMitigationSettings")



@_attrs_define
class CircuitJobErrorMitigationSettings:
    """ 
        Attributes:
            debiasing (bool | JsonObject | Unset):
            symmetry_verification (bool | JsonObject | None | Unset):
     """

    debiasing: bool | JsonObject | Unset = UNSET
    symmetry_verification: bool | JsonObject | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.json_object import JsonObject
        debiasing: bool | dict[str, Any] | Unset
        if isinstance(self.debiasing, Unset):
            debiasing = UNSET
        elif isinstance(self.debiasing, JsonObject):
            debiasing = self.debiasing.to_dict()
        else:
            debiasing = self.debiasing

        symmetry_verification: bool | dict[str, Any] | None | Unset
        if isinstance(self.symmetry_verification, Unset):
            symmetry_verification = UNSET
        elif isinstance(self.symmetry_verification, JsonObject):
            symmetry_verification = self.symmetry_verification.to_dict()
        else:
            symmetry_verification = self.symmetry_verification


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if debiasing is not UNSET:
            field_dict["debiasing"] = debiasing
        if symmetry_verification is not UNSET:
            field_dict["symmetry_verification"] = symmetry_verification

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.json_object import JsonObject
        d = dict(src_dict)
        def _parse_debiasing(data: object) -> bool | JsonObject | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                debiasing_type_1 = JsonObject.from_dict(data)



                return debiasing_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(bool | JsonObject | Unset, data)

        debiasing = _parse_debiasing(d.pop("debiasing", UNSET))


        def _parse_symmetry_verification(data: object) -> bool | JsonObject | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                symmetry_verification_type_1 = JsonObject.from_dict(data)



                return symmetry_verification_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(bool | JsonObject | None | Unset, data)

        symmetry_verification = _parse_symmetry_verification(d.pop("symmetry_verification", UNSET))


        circuit_job_error_mitigation_settings = cls(
            debiasing=debiasing,
            symmetry_verification=symmetry_verification,
        )

        return circuit_job_error_mitigation_settings

