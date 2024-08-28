import React, { useState } from 'react';
import { View, Text, TouchableOpacity, Alert, TouchableWithoutFeedback } from 'react-native';
import { WebView } from 'react-native-webview';
import axios from 'axios';
import { Ionicons } from '@expo/vector-icons'; // Import Ionicons from @expo/vector-icons
import { handleNextSlide, handlePrevSlide, handleShowScreen } from './api';
import styles from './styles';

const App = () => {
  const [showScreen, setShowScreen] = useState(false);
  const [isMenuVisible, setIsMenuVisible] = useState(false);

  const toggleMenu = () => {
    setIsMenuVisible(!isMenuVisible);
  };

  const closeMenu = () => {
    if (isMenuVisible) {
      setIsMenuVisible(false);
    }
  };

  return (
    <TouchableWithoutFeedback onPress={closeMenu}>
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
    </TouchableWithoutFeedback>
  );
};

export default App;