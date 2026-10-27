from unittest.mock import patch

from app import check_health, main


def test_healthy_system():
    result = check_health(20, 40, 50)
    assert result == "HEALTHY"


def test_high_cpu():
    result = check_health(90, 40, 50)
    assert result == "WARNING"


def test_high_memory():
    result = check_health(20, 90, 50)
    assert result == "WARNING"


def test_high_disk():
    result = check_health(20, 40, 90)
    assert result == "WARNING"


def test_all_usage_high():
    result = check_health(90, 90, 90)
    assert result == "WARNING"


@patch("app.psutil.disk_usage")
@patch("app.psutil.virtual_memory")
@patch("app.psutil.cpu_percent")
def test_main_healthy(mock_cpu, mock_memory, mock_disk, capsys):
    mock_cpu.return_value = 20
    mock_memory.return_value.percent = 40
    mock_disk.return_value.percent = 50

    main()

    output = capsys.readouterr().out

    assert "System Health" in output
    assert "CPU Usage    : 20%" in output
    assert "Memory Usage : 40%" in output
    assert "Disk Usage   : 50%" in output
    assert "Status       : HEALTHY" in output


@patch("app.psutil.disk_usage")
@patch("app.psutil.virtual_memory")
@patch("app.psutil.cpu_percent")
def test_main_warning(mock_cpu, mock_memory, mock_disk, capsys):
    mock_cpu.return_value = 90
    mock_memory.return_value.percent = 40
    mock_disk.return_value.percent = 50

    main()

    output = capsys.readouterr().out

    assert "Status       : WARNING" in output