import React, {useEffect, useState} from 'react';
import {SafeAreaView, Text, View, Button} from 'react-native';
import {BleManager} from 'react-native-ble-plx';

const TELEMETRY_SERVICE = "8f264f10-7d3c-4c8f-9a2e-3b0a0b6c1111";
const RESULT_CHAR = "8f264f11-7d3c-4c8f-9a2e-3b0a0b6c1111";

const manager = new BleManager();

export default function App() {
  const [device, setDevice] = useState(null);
  const [data, setData] = useState({classId: 0, confidence: 0, size: 0, texture: 0});

  const scan = async () => {
    manager.startDeviceScan(null, null, async (error, dev) => {
      if (error) return;
      if (dev && dev.name === 'EchoGrip') {
        manager.stopDeviceScan();
        const d = await dev.connect();
        await d.discoverAllServicesAndCharacteristics();
        setDevice(d);
        d.monitorCharacteristicForService(TELEMETRY_SERVICE, RESULT_CHAR, (err, char) => {
          if (err || !char?.value) return;
          const b = Buffer.from(char.value, 'base64');
          const view = new DataView(b.buffer, b.byteOffset, b.byteLength);
          const classId = view.getInt16(0, true);
          const conf = view.getUint16(2, true) / 256.0;
          const size = view.getUint16(4, true) / 256.0;
          const texture = view.getUint16(6, true) / 256.0;
          setData({classId, confidence: conf, size, texture});
        });
      }
    });
  };

  return (
    <SafeAreaView style={{flex:1, padding:16}}>
      <Button title={device ? 'Connected' : 'Scan & Connect'} onPress={scan} />
      <View style={{marginTop:24}}>
        <Text>Class: {data.classId}</Text>
        <Text>Confidence: {data.confidence.toFixed(2)}</Text>
        <Text>Size: {data.size.toFixed(2)}</Text>
        <Text>Texture: {data.texture.toFixed(2)}</Text>
      </View>
    </SafeAreaView>
  );
}


