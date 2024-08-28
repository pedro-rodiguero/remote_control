import axios from 'axios';
import { Alert } from 'react-native';

export const fetchServerIp = async () => {
  try {
    const response = await axios.get('http://127.0.0.1:5000/get_ip'); // Use localhost initially
    const ip = response.data.ip;
    console.log(`Fetched Server IP: ${ip}`); // Log the fetched IP for debugging
    return ip;
  } catch (error) {
    Alert.alert('Error fetching server IP');
    return '127.0.0.1'; // Default value in case of error
  }
};

export const handleNextSlide = async (serverIp: string) => {
  try {
    await axios.get(`http://${serverIp}:5000/next`);
    Alert.alert('Moved to Next Slide');
  } catch (error) {
    Alert.alert('Error moving to next slide');
  }
};

export const handlePrevSlide = async (serverIp: string) => {
  try {
    await axios.get(`http://${serverIp}:5000/prev`);
    Alert.alert('Moved to Previous Slide');
  } catch (error) {
    Alert.alert('Error moving to previous slide. IP: ' + serverIp);
  }
};

export const handleShowScreen = async (serverIp: string) => {
  try {
    await axios.get(`http://${serverIp}:5000/show_screen`);
    Alert.alert('Screen is now showing');
  } catch (error) {
    Alert.alert('Error showing screen');
  }
};

// You can add more API functions here as needed