import React, { useState } from 'react';
import { View, Text, TouchableOpacity, Alert, StyleSheet } from 'react-native';
import { WebView } from 'react-native-webview';
import axios from 'axios';
import { Ionicons } from '@expo/vector-icons'; // Import Ionicons from @expo/vector-icons
import { handleNextSlide, handlePrevSlide, handleShowScreen } from './api';

const App = () => {
  const [showScreen, setShowScreen] = useState(false);
  const [isMenuVisible, setIsMenuVisible] = useState(false);

  const toggleMenu = () => {
    setIsMenuVisible(!isMenuVisible);
  };

  return (
    <View style={styles.container}>
      <TouchableOpacity style={styles.menuButton} onPress={toggleMenu}>
        <Ionicons name="menu" size={32} color="black" />
      </TouchableOpacity>
      {isMenuVisible && (
        <View style={styles.sideMenu}>
          <Text style={styles.menuItem}>Menu Item 1</Text>
          <Text style={styles.menuItem}>Menu Item 2</Text>
          <Text style={styles.menuItem}>Menu Item 3</Text>
        </View>
      )}
      {showScreen ? (
        <WebView source={{ uri: 'http://localhost:5000/screen' }} style={{ flex: 1 }} /> // Change to church computer's IP address
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
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
  menuButton: {
    position: 'absolute',
    top: 40,
    left: 20,
  },
  sideMenu: {
    position: 'absolute',
    top: 80,
    left: 0,
    width: 200,
    backgroundColor: 'white',
    padding: 10,
    borderColor: 'black',
    borderWidth: 1,
  },
  menuItem: {
    padding: 10,
    borderBottomColor: 'black',
    borderBottomWidth: 1,
  },
  button: {
    margin: 10,
    padding: 10,
    backgroundColor: 'blue',
    borderRadius: 5,
  },
  buttonText: {
    color: 'white',
    fontSize: 16,
  },
});

export default App;