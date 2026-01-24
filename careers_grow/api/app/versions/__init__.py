from careers_grow.api.app.versions.v1 import V1
from careers_grow.api.app.versions.v2 import V2

VERSION_MAP = {
	"v1": V1(),
	"v2": V2(),
}
