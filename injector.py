# Usage: mitmdump -s "js_injector.py src"
# (this script works best with --anticache)
from bs4 import BeautifulSoup
from mitmproxy import ctx, http


class Injector:
    def load(self, loader):
        loader.add_option(
            "scr_url", str, "", "script_url to inject"
        )

    def response(self, flow: http.HTTPFlow) -> None:
        if ctx.options.scr_url:
            html = BeautifulSoup(flow.response.content, "html.parser")
            if html.body:
                script = html.new_tag(
                    "script",
                    src=context.src_url,
                    type='application/javascript')
                html.body.insert(0, script)
                flow.response.content = str(html).encode("utf8")
                context.log("Script injected.")


addons = [Injector()]
