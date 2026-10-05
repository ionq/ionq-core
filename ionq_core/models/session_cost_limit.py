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






T = TypeVar("T", bound="SessionCostLimit")



@_attrs_define
class SessionCostLimit:
    """ 
        Attributes:
            value (float):
            unit (str | Unset):
     """

    value: float
    unit: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        value = self.value

        unit = self.unit


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "value": value,
        })
        if unit is not UNSET:
            field_dict["unit"] = unit

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        value = d.pop("value")

        unit = d.pop("unit", UNSET)

        session_cost_limit = cls(
            value=value,
            unit=unit,
        )

        return session_cost_limit

