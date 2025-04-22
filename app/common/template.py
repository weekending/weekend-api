from starlette.templating import Jinja2Templates

from .utils import urlx_for


template = Jinja2Templates("app/adapter/inbound/web/templates/")
template.env.globals["url_for"] = urlx_for
