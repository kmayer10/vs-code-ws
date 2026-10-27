from app import check_health


def test_healthy_system():
    assert check_health(30, 40, 50) == "HEALTHY"


def test_high_cpu():
    assert check_health(90, 40, 50) == "WARNING"


def test_high_memory():
    assert check_health(30, 90, 50) == "WARNING"


def test_high_disk():
    assert check_health(30, 40, 90) == "WARNING"
