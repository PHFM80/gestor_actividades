import json
import logging
from datetime import datetime, timezone


logger = logging.getLogger("complementos_audit")


def _client_ip(request):
    forwarded = request.META.get("HTTP_X_FORWARDED_FOR", "")
    if forwarded:
        return forwarded.split(",")[0].strip()
    return request.META.get("REMOTE_ADDR", "")


def _snapshot_from_cleaned_data(cleaned_data):
    snapshot = {}
    for key, value in cleaned_data.items():
        if hasattr(value, "pk"):
            snapshot[key] = value.pk
        else:
            snapshot[key] = value
    return snapshot


def _diff(before, after):
    before = before or {}
    after = after or {}
    keys = set(before.keys()) | set(after.keys())
    changed = {}
    for key in sorted(keys):
        if before.get(key) != after.get(key):
            changed[key] = {
                "before": before.get(key),
                "after": after.get(key),
            }
    return changed


def log_complemento_event(
    *,
    request,
    event,
    complemento_tipo,
    status,
    model_name,
    registro_id=None,
    before=None,
    after=None,
    errors=None,
):
    user = getattr(request, "user", None)
    payload = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "event": event,
        "complemento_tipo": complemento_tipo,
        "model_name": model_name,
        "registro_id": registro_id,
        "usuario_id": getattr(user, "id", None),
        "usuario_email": getattr(user, "email", None),
        "ip": _client_ip(request),
        "request_id": request.META.get("HTTP_X_REQUEST_ID"),
        "origen": request.path,
        "metodo": request.method,
        "estado": status,
        "cambios": _diff(before, after),
        "errores": errors or {},
    }
    logger.info(json.dumps(payload, ensure_ascii=False, default=str))


def cleaned_data_snapshot(form):
    return _snapshot_from_cleaned_data(form.cleaned_data)
