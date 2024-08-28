import axios from 'axios';
import { Alert } from 'react-native';

export const handleNextSlide = async () => {
  try {
    await axios.get('http://localhost:5000/next'); // Change to church computer's IP address
    Alert.alert('Moved to Next Slide');
  } catch (error) {
    Alert.alert('Error moving to next slide');
  }
};

export const handlePrevSlide = async () => {
    try {
        await axios.get('http://localhost:5000/prev'); // Change to church computer's IP address
        Alert.alert('Moved to Previous Slide');
    } catch (error) {
        Alert.alert('Error moving to previous slide');
    }
}

export const handleShowScreen = async () => {
    try {
        await axios.get('http://localhost:5000/show_screen'); // Change to church computer's IP address
        Alert.alert('Screen is now showing');
    } catch (error) {
        Alert.alert('Error showing screen');
    }
}

// You can add more API functions here as needed