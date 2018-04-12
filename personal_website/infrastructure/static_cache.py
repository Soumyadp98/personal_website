import hashlib
import os

__full_path = os.path.dirname(os.path.abspath(__file__))
__hash_lookup = dict()

# Set this to False in production, True in development
recompute_caches_every_request = True
enable_tracing = False


def build_cache_id(relative_file_url: str):
    if not relative_file_url:
        return "ERROR_NO_FILE_SPECIFIED"

    # Can we use a precomputed version?
    use_hash = not recompute_caches_every_request
    key = relative_file_url

    if use_hash and key in __hash_lookup:
        __trace("Using cached lookup for {} -> {}".format(key, __hash_lookup[key]))
        return __hash_lookup[key]

    fullname = os.path.abspath(os.path.join(
        __full_path, relative_file_url.lstrip('/')))

    if not os.path.exists(fullname):
        return "ERROR_MISSING_FILE"

    digest_value = __get_file_hash(fullname)
    __hash_lookup[key] = digest_value

    __trace("Computed digest for {} -> {}".format(key, __hash_lookup[key]))
    return digest_value


def __get_file_hash(filename):
    md5 = hashlib.md5()

    with open(filename, 'rb') as fin:
        data = fin.read()
        md5.update(data)

    return md5.hexdigest()


def __trace(text):
    # This is really for just seeing things in action.
    # You might want real logging...
    if not enable_tracing:
        return

    print(text)
