from django.core import signing
from django.conf import settings

from apps.queues.models import Token


def sign_token(token: Token) -> str:
    return signing.dumps(
        {"k": token.public_key},
        salt=settings.PATIENT_LINK_SALT,
        compress=True,
    )


def resolve_signed(value: str) -> Token | None:
    try:
        data = signing.loads(
            value,
            salt=settings.PATIENT_LINK_SALT,
            max_age=settings.PATIENT_LINK_MAX_AGE,
        )
    except signing.BadSignature:
        return None
    key = data.get("k") if isinstance(data, dict) else None
    if not key:
        return None
    return Token.objects.filter(public_key=key).select_related("doctor", "clinic").first()
