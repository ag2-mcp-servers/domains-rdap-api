# generated by fastapi-codegen:
#   filename:  openapi.yaml
#   timestamp: 2025-06-29T02:01:05+00:00

from __future__ import annotations

from enum import Enum
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field


class HttpBody(BaseModel):
    contentType: Optional[str] = Field(
        None,
        description='The HTTP Content-Type header value specifying the content type of the body.',
    )
    data: Optional[str] = Field(
        None, description='The HTTP request/response body as raw binary.'
    )
    extensions: Optional[List[Dict[str, Any]]] = Field(
        None,
        description='Application specific response metadata. Must be set in the first response for streaming APIs.',
    )


class Link(BaseModel):
    href: Optional[str] = Field(
        None,
        description='Target URL of a link. Example: "http://example.com/previous".',
    )
    hreflang: Optional[str] = Field(
        None, description='Language code of a link. Example: "en".'
    )
    media: Optional[str] = Field(
        None, description='Media type of the link destination. Example: "screen".'
    )
    rel: Optional[str] = Field(
        None, description='Relation type of a link. Example: "previous".'
    )
    title: Optional[str] = Field(
        None, description='Title of this link. Example: "title".'
    )
    type: Optional[str] = Field(
        None, description='Content type of the link. Example: "application/json".'
    )
    value: Optional[str] = Field(
        None,
        description='URL giving context for the link. Example: "http://example.com/current".',
    )


class Notice(BaseModel):
    description: Optional[List[str]] = Field(
        None, description='Description of the notice.'
    )
    links: Optional[List[Link]] = Field(
        None, description='Link to a document containing more information.'
    )
    title: Optional[str] = Field(
        None, description='Title of a notice. Example: "Terms of Service".'
    )
    type: Optional[str] = Field(
        None,
        description='Type values defined in [section 10.2.1 of RFC 7483](https://tools.ietf.org/html/rfc7483#section-10.2.1) specific to a whole response: "result set truncated due to authorization", "result set truncated due to excessive load", "result set truncated due to unexplainable reasons".',
    )


class RdapResponse(BaseModel):
    description: Optional[List[str]] = Field(None, description='Error description.')
    errorCode: Optional[int] = Field(
        None, description='Error HTTP code. Example: "501".'
    )
    jsonResponse: Optional[HttpBody] = Field(
        None,
        description='HTTP response with content type set to "application/json+rdap".',
    )
    lang: Optional[str] = Field(
        None,
        description='Error language code. Error response info fields are defined in [section 6 of RFC 7483](https://tools.ietf.org/html/rfc7483#section-6).',
    )
    notices: Optional[List[Notice]] = Field(
        None, description='Notices applying to this response.'
    )
    rdapConformance: Optional[List[str]] = Field(
        None, description='RDAP conformance level.'
    )
    title: Optional[str] = Field(None, description='Error title.')


class FieldXgafv(Enum):
    field_1 = '1'
    field_2 = '2'


class Alt(Enum):
    json = 'json'
    media = 'media'
    proto = 'proto'
