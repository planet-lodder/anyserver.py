import os
from anyserver import WebRouter
from anyserver.templates import TemplateRouter

THIS_DIR = os.path.dirname(os.path.realpath(__file__))

# Create decorator for registering web routes
router = TemplateRouter('/test', base=f'{THIS_DIR}/templates')


@router.get('')
@router.renders('test/index')
def GetStatus(req, resp):
    return {
        "status": "online",
    }


@router.post('')
def PostStatus(req, resp):
    return {
        "verb": req.verb,
    }


@router.put('')
def PutStatus(req, resp):
    return {
        "verb": req.verb,
    }

@router.delete('')
def PutStatus(req, resp):
    return {
        "verb": req.verb,
    }