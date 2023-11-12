__version__ = "16.1.2"
__package_version__ = __version__


# Handle version suffix for nightly, just like tutor core.
__version_suffix__ = "edspirit"

if __version_suffix__:
    __version__ += "-" + __version_suffix__
