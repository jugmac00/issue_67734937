from main import Settings


def test_settings():
    settings = Settings(_env_file=".env")
    assert settings.environment == "production"
