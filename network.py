import uuid
import NetworkManager
import dbus.mainloop.glib
import time

hotspot = {'802-11-wireless': {
    'band': 'bg',
    'mode': 'ap',
    'security': '802-11-wireless-security',
    'ssid': 'Parkspot'},
    '802-11-wireless-security': {'key-mgmt': 'wpa-psk', 'psk': 'parkspot'},
    'connection': {
        'autoconnect': False,
        'id': 'Parkspot_AP',
        'type': '802-11-wireless',
        'uuid': str(uuid.uuid4())},
    'ipv4': {'method': 'shared'},
    'ipv6': {'method': 'shared'}}

wifi = {
    '802-11-wireless': {
        'mode': 'infrastructure',
        'security': '802-11-wireless-security',
        'ssid': ''},
    '802-11-wireless-security': {
        'auth-alg': 'open',
        'key-mgmt': 'wpa-psk',
        'psk': ''},
    'connection': {
        'id': '',
        'type': '802-11-wireless',
        'uuid': str(uuid.uuid4())},
    'ipv4': {'method': 'auto'},
    'ipv6': {'method': 'auto'}}

connection_id = 'Parkspot_AP'


class Network():
    def __init__(self):
        dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)
        conn = self.getConnection(connection_id)
        if conn is None:
            hotspot['802-11-wireless']['ssid'] = "Parkspot_" + \
                self.getWifiDevice().HwAddress.replace(":", "")
            NetworkManager.Settings.AddConnection(hotspot)

        self.wifi = wifi

    def getConnection(self, s_id):
        connections = NetworkManager.Settings.ListConnections()
        connections = dict([(x.GetSettings()['connection']['id'], x)
                            for x in connections])
        if s_id in connections:
            print("Found Connection")
            return connections[s_id]
        else:
            print("Could not find Connection")
            return None

    def getWifiDevice(self):
        for dev in NetworkManager.Device.all():
            if dev.DeviceType == NetworkManager.NM_DEVICE_TYPE_WIFI:
                print("Found WIFI Device")
                return dev.SpecificDevice()

    def getAccesspoints(self):
        ssids = {}
        while len(ssids) == 0:
            print("Searching APs")
            for ap in NetworkManager.AccessPoint.all():
                ssids[ap.Ssid] = ap.Strength

        return ssids

    def createAccessPoint(self):
        conn = self.getConnection('Parkspot_AP')
        self.connect(conn)

    def connect(self, conn):
        active_conn = NetworkManager.NetworkManager.ActivateConnection(
            conn, self.getWifiDevice(), "/")
        time.sleep(10)
        if active_conn.State == NetworkManager.NM_ACTIVE_CONNECTION_STATE_ACTIVATED:
            print("Succesfully connected")
            return True
        else:
            print("Could not connect")
            self.disconnect()
            return False

    def disconnect(self):
        print("Disconnect WIFI Device")
        try:
            self.getWifiDevice().Disconnect()
            time.sleep(1)
            return
        except Exception:
            return
