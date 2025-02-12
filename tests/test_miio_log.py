from custom_components.xiaomi_gateway3.core.gateway import miot


def test_gw_heartbeat():
    raw = b'[20211014 09:23:50] [D] ot_agent_recv_handler_one(): fd:13, msg:{"method":"local.query_time","id":151592}{"method":"event.gw.heartbeat","params":[{"free_mem":11872,"ip":"192.168.1.123","load_avg":"1.24|1.39|1.38|4\\/88|720","rssi":58,"run_time":358537,"ssid":"WiFi"}],"id":151593} length:216 bytes'
    p = miot.decode_miio_json(raw, b"event.gw.heartbeat")
    assert len(p) == 1 and p[0]["params"][0]["free_mem"] == 11872


def test_properties_changed():
    raw = b'[20211014 09:54:22] [D] ot_agent_recv_handler_one(): fd:13, msg:{"method":"properties_changed","params":[{"did":"<10 numb>","siid":2,"piid":1,"value":true}],"id":152814} length:106 bytes'
    p = miot.decode_miio_json(raw, b"properties_changed")
    assert p[0]["params"][0]["siid"] == 2


def test_ble_event():
    raw = b'[20211014 09:20:28] [D] ot_agent_recv_handler_one(): fd:13, msg:{"method":"_async.ble_event","params":{"dev":{"did":"blt.3.<alphanum>","mac":"<mac>","pdid":2038},"evt":[{"eid":4119,"edata":"00000000"}],"frmCnt":233,"gwts":1634192427},"id":151482} length:197 bytes'
    p = miot.decode_miio_json(raw, b"_async.ble_event")
    assert p[0]["params"]["dev"]["pdid"] == 2038
