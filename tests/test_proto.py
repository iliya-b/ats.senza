import pytest

from ats.senza.server.protocol import (accelerometer, battery, gps, gravity, gyroscope,
                                       light, linear_acc, magnetometer, orientation,
                                       proximity, pressure, relative_humidity,
                                       temperature, camera, rotation_vector)


class FakeApp:
    config = {'camera': {'video_path': '/test/camera/'}}
    async def send_event(self, routing_key, payload, paylog):
        pass


class MockRequest:
    __slots__ = ['_data', 'match_info', 'app']

    def __init__(self, **kwargs):
        self._data = kwargs
        self.match_info = {'avm_id': 'test'}
        self.app = FakeApp()

    async def json(self):
        print('awaited')
        return self._data

    def __repr__(self):
        return 'MockRequest(%s)' % repr(self._data)


class MockResponse:
    def __init__(self, *args, **kwargs):
        self.data = kwargs

    def __getattr__(self, name):
        return getattr(self, 'data')[name]

    def __repr__(self):
        return 'MockResponse(%s)' % self.data


def req_ok(response):
    return response.status == 204


def float_range(*args):
    return map(lambda x: float(x), range(*args))


@pytest.fixture(autouse=True)
def no_aiohttp(monkeypatch):
    monkeypatch.setattr('aiohttp.web.Response', MockResponse)


@pytest.mark.parametrize('fake_request',
                         [MockRequest(x=i, y=i, z=i) for i in float_range(10)])
@pytest.mark.asyncio
async def test_accelerometer(fake_request):
    result = await accelerometer.Producer().post_handler(fake_request)
    assert result.status == 204


@pytest.mark.parametrize('fake_request',
                         [MockRequest(azimuth=i, pitch=i, roll=i) for i in float_range(10)])
@pytest.mark.asyncio
async def test_gyroscope(fake_request):
    result = await gyroscope.Producer().post_handler(fake_request)
    assert result.status == 204


@pytest.mark.parametrize('fake_request',
                         [MockRequest(x=i, y=i, z=i) for i in float_range(10)])
@pytest.mark.asyncio
async def test_magnetometer(fake_request):
    result = await magnetometer.Producer().post_handler(fake_request)
    assert result.status == 204


@pytest.mark.parametrize('fake_request',
                         [MockRequest(x=i, y=i, z=i) for i in float_range(10)])
@pytest.mark.asyncio
async def test_gravity(fake_request):
    result = await gravity.Producer().post_handler(fake_request)
    assert result.status == 204


@pytest.mark.parametrize('fake_request',
                         [MockRequest(x=i, y=i, z=i) for i in float_range(10)])
@pytest.mark.asyncio
async def test_linear_acc(fake_request):
    result = await linear_acc.Producer().post_handler(fake_request)
    assert result.status == 204


@pytest.mark.parametrize('fake_request',
                         [MockRequest(level_percent=i, ac_online=1) for i in range(1, 101, 10)])
@pytest.mark.asyncio
async def test_battery(fake_request):
    result = await battery.Producer().post_handler(fake_request)
    assert result.status == 204


@pytest.mark.parametrize('fake_request',
                         [MockRequest(latitude=i, longitude=i) for i in float_range(0, 50, 5)])
@pytest.mark.asyncio
async def test_gps(fake_request):
    result = await gps.Producer().post_handler(fake_request)
    assert result.status == 204


@pytest.mark.parametrize('fake_request', [MockRequest(latitude=91, longitude=-181)])
@pytest.mark.asyncio
async def test_gps_failed(fake_request):
    result = await gps.Producer().post_handler(fake_request)
    assert result.status == 400


@pytest.mark.parametrize('fake_request',
                         [MockRequest(distance=i) for i in range(0, 100, 10)])
@pytest.mark.asyncio
async def test_proximity(fake_request):
    result = await proximity.Producer().post_handler(fake_request)
    assert result.status == 204


@pytest.mark.parametrize('fake_request',
                         [MockRequest(relative_humidity=i) for i in range(0, 100, 10)])
@pytest.mark.asyncio
async def test_humidity(fake_request):
    result = await relative_humidity.Producer().post_handler(fake_request)
    assert result.status == 204


@pytest.mark.parametrize('fake_request',
                         [MockRequest(temperature=i) for i in range(0, 100, 10)])
@pytest.mark.asyncio
async def test_temperature(fake_request):
    result = await temperature.Producer().post_handler(fake_request)
    assert result.status == 204


@pytest.mark.parametrize('fake_request',
                         [MockRequest(pressure=i) for i in range(0, 100, 10)])
@pytest.mark.asyncio
async def test_pressure(fake_request):
    result = await pressure.Producer().post_handler(fake_request)
    assert result.status == 204


@pytest.mark.parametrize('fake_request', [MockRequest(pressure=-1)])
@pytest.mark.asyncio
async def test_pressure_badrequest(fake_request):
    result = await pressure.Producer().post_handler(fake_request)
    assert result.status == 400


@pytest.mark.parametrize('fake_request',
                         [MockRequest(light=i) for i in range(0, 100, 10)])
@pytest.mark.asyncio
async def test_light(fake_request):
    result = await light.Producer().post_handler(fake_request)
    assert result.status == 204


@pytest.mark.parametrize('fake_request',
                         [MockRequest(azimuth=i, pitch=i, roll=i) for i in float_range(10)])
@pytest.mark.asyncio
async def test_orientation(fake_request):
    result = await orientation.Producer().post_handler(fake_request)
    assert result.status == 204


@pytest.mark.asyncio
async def test_camera():
    req = MockRequest(file_id="test.mp4")
    result = await camera.Producer().post_handler(req)
    assert result.status == 204

    req = MockRequest(file_id="/test/test.mp4")
    with pytest.raises(Exception):
        result = await camera.Producer().post_handler(req)

    req = MockRequest(file_id="../../test.mp4")
    with pytest.raises(Exception):
        result = await camera.Producer().post_handler(req)


@pytest.mark.parametrize('fake_request',
                         [MockRequest(x=i, y=i, z=i, angle=i, accuracy=i) for i in float_range(10)])
@pytest.mark.asyncio
async def test_rotation_vector(fake_request):
    result = await rotation_vector.Producer().post_handler(fake_request)
    assert result.status == 204
