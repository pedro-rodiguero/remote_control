import React, { useState } from 'react';
import { Text, View, Alert, TouchableOpacity } from 'react-native';
import axios from 'axios';
import styles from './styles'; // Import the styles
import { WebView } from 'react-native-webview'; // Import WebView

export default function App() {
  const [showScreen, setShowScreen] = useState(false);

  const handleNextSlide = async () => {
    try {
      await axios.get('http://localhost:5000/next'); // Change to church computer's IP address
      Alert.alert('Moved to Next Slide');
    } catch (error) {
      Alert.alert('Error moving to next slide');
    }
  };

  const handlePrevSlide = async () => {
    try {
      await axios.get('http://localhost:5000/prev'); // Change to church computer's IP address
      Alert.alert('Moved to Previous Slide');
    } catch (error) {
      Alert.alert('Error moving to previous slide');
    }
  };

  const handleShowScreen = async () => {
    try {
      await axios.get('http://localhost:5000/show_screen'); // Change to church computer's IP address
      setShowScreen(true);
    } catch (error) {
      Alert.alert('Error showing screen');
    }
  };

  return (
    <View style={styles.container}>
      {showScreen ? (
        <WebView source={{ uri: 'http://localhost:5000/screen' }} style={{ flex: 1 }} />
      ) : (
        <>
          <TouchableOpacity style={styles.button} onPress={handleNextSlide} activeOpacity={0.7}>
            <Text style={styles.buttonText}>Next Slide</Text>
          </TouchableOpacity>
          <TouchableOpacity style={styles.button} onPress={handlePrevSlide} activeOpacity={0.7}>
            <Text style={styles.buttonText}>Previous Slide</Text>
          </TouchableOpacity>
          <TouchableOpacity style={styles.button} onPress={handleShowScreen} activeOpacity={0.7}>
            <Text style={styles.buttonText}>Show Screen</Text>
          </TouchableOpacity>
        </>
      )}
    </View>
  );
}