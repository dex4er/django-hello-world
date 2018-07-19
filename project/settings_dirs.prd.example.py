# Default directories

import os

# /home/<app>/site
SITE_DIR = os.path.realpath(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

# /home/<app>/site/base
BASE_DIR = os.path.realpath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# /home/<app>/site/base/<project>
PROJECT_DIR = os.path.realpath(os.path.dirname(os.path.abspath(__file__)))
PROJECT_DIRNAME = PROJECT_DIR.split(os.sep)[-1]