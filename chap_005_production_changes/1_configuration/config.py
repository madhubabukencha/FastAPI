from dynaconf import Dynaconf

settings = Dynaconf(
    envvar_prefix="SERVER",
    settings_files=["settings.yaml", ".secrets.yaml"],
)