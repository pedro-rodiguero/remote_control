import React from 'react';
import { StyleSheet, Text, View, Button, Alert } from 'react-native';
import axios from 'axios';

export default function App() {
  const handleNextSlide = async () => {
    try {
      await axios.get('http://<YOUR_SERVER_IP>:5000/next');
      Alert.alert('Moved to Next Slide');
    } catch (error) {
      Alert.alert('Error moving to next slide');
    }
  };

  const handlePrevSlide = async () => {
    try {
      await axios.get('http://<YOUR_SERVER_IP>:5000/prev');
      Alert.alert('Moved to Previous Slide');
    } catch (error) {
      Alert.alert('Error moving to previous slide');
    }
  };

  const handleShowMenu = async () => {
    try {
      await axios.get('http://<YOUR_SERVER_IP>:5000/menu');
      Alert.alert('Menu Shown');
    } catch (error) {
      Alert.alert('Error showing menu');
    }
  };

  return (
    <View style={styles.container}>
      <Button title="Next Slide" onPress={handleNextSlide} />
      <Button title="Previous Slide" onPress={handlePrevSlide} />
      <Button title="Show Menu" onPress={handleShowMenu} />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
});