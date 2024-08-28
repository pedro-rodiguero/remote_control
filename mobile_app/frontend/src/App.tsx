import React, { useState, useEffect } from 'react';
import { View, Text, TouchableOpacity, Alert, TouchableWithoutFeedback, Image, Button } from 'react-native';
import { WebView } from 'react-native-webview';
import { Ionicons } from '@expo/vector-icons';
import { handleNextSlide, handlePrevSlide, handleShowScreen, fetchServerIp } from './api';
import styles from './styles';
import { Camera, CameraView, BarcodeScanningResult, useCameraPermissions } from 'expo-camera';

const App = () => {
  const [showScreen, setShowScreen] = useState(false);
  const [isMenuVisible, setIsMenuVisible] = useState(false);
  const [scanned, setScanned] = useState(false);
  const [serverIp, setServerIp] = useState('127.0.0.1'); // Default value
  const [facing, setFacing] = useState<'back' | 'front'>('back');
  const [permission, requestPermission] = useCameraPermissions();

  useEffect(() => {
    fetchServerIp().then(ip => setServerIp(ip));
  }, []);

  const toggleMenu = () => {
    setIsMenuVisible(!isMenuVisible);
  };

  const closeMenu = () => {
    if (isMenuVisible) {
      setIsMenuVisible(false);
    }
  };

  const handleBarCodeScanned = ({ type, data }: BarcodeScanningResult) => {
    setScanned(true);
    setServerIp(data); // Use setServerIp to update the state
    Alert.alert(`Server IP set to: ${data}`);
  };

  if (!permission) {
    // Camera permissions are still loading.
    return <View />;
  }

  if (!permission.granted) {
    // Camera permissions are not granted yet.
    return (
      <View style={styles.container}>
        <Text style={styles.message}>We need your permission to show the camera</Text>
        <Button onPress={requestPermission} title="grant permission" />
      </View>
    );
  }

  return (
    <TouchableWithoutFeedback onPress={closeMenu}>
      <View style={styles.container}>
        <TouchableOpacity style={styles.menuButton} onPress={toggleMenu}>
          <Ionicons name="menu" size={32} color="black" />
        </TouchableOpacity>
        <Image source={require('../assets/icon.png')} style={styles.icon} />
        {isMenuVisible && (
          <View style={styles.sideMenu}>
            <Text style={styles.menuItem}>Menu Item 1</Text>
            <Text style={styles.menuItem}>Menu Item 2</Text>
            <Text style={styles.menuItem}>Menu Item 3</Text>
          </View>
        )}
        {showScreen ? (
          <WebView source={{ uri: `http://${serverIp}:5000/screen` }} style={{ flex: 1 }} />
        ) : (
          <>
            <TouchableOpacity style={styles.button} onPress={() => handleNextSlide(serverIp)} activeOpacity={0.7}>
              <Text style={styles.buttonText}>Next Slide</Text>
            </TouchableOpacity>
            <TouchableOpacity style={styles.button} onPress={() => handlePrevSlide(serverIp)} activeOpacity={0.7}>
              <Text style={styles.buttonText}>Previous Slide</Text>
            </TouchableOpacity>
            <TouchableOpacity style={styles.button} onPress={() => handleShowScreen(serverIp)} activeOpacity={0.7}>
              <Text style={styles.buttonText}>Show Screen</Text>
            </TouchableOpacity>
            <TouchableOpacity style={styles.button} onPress={() => setScanned(false)} activeOpacity={0.7}>
              <Text style={styles.buttonText}>Scan QR Code</Text>
            </TouchableOpacity>
            {!scanned && (
              <CameraView
                onBarcodeScanned={scanned ? undefined : handleBarCodeScanned}
                style={{ height: 200, width: 200 }}
                facing={facing}
                barcodeScannerSettings={{
                  barcodeTypes: ["qr"],
                }}
              >
                <View style={styles.buttonContainer}>
                  <TouchableOpacity style={styles.button} onPress={() => setFacing(current => (current === 'back' ? 'front' : 'back'))}>
                    <Text style={styles.text}>Flip Camera</Text>
                  </TouchableOpacity>
                </View>
              </CameraView>
            )}
          </>
        )}
      </View>
    </TouchableWithoutFeedback>
  );
};

export default App;