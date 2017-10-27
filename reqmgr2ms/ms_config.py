"""
MicroService configuration file.
"""

import os
import socket
from WMCore.Configuration import Configuration

# globals
HOST = socket.gethostname().lower()
LOG_REPORTER = "reqmgr2-ms"
ROOTDIR = __file__.rsplit('/', 3)[0]
config = Configuration()

main = config.section_("main")
srv = main.section_("server")
srv.thread_pool = 30
main.application = "microservice"
main.port = 8248  # main application port it listens on
main.index = 'data' # Configuration requires index attribute

# Security configuration
main.authz_defaults = {"role": None, "group": None, "site": None}
sec = main.section_("tools").section_("cms_auth")
sec.key_file = "%s/auth/wmcore-auth/header-auth-key" % ROOTDIR

# this is where the application will be mounted, where the REST API
# is reachable and this features in CMS web frontend rewrite rules
app = config.section_(main.application)
app.admin = "cms-service-webtools@cern.ch"
app.description = "CMS data operations MicroService"
app.title = "CMS MicroService"

# define different views for our application
views = config.section_("views")
# web UI interface
ui = views.section_('web') # was section 'ui'
ui.object = 'WMCore.Services.MicroService.FrontPage.FrontPage'
ui.static = ROOTDIR

# REST interface
data = views.section_('data')
data.object = 'WMCore.Services.MicroService.RestApi.RestInterface'
data.manager = 'WMCore.Services.MicroService.Unified.Transferor.UnifiedTransferorManager'
