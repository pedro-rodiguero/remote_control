import { StyleSheet } from 'react-native';

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
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
    backgroundColor: '#007BFF',
    padding: 15,
    borderRadius: 5,
    marginVertical: 10,
    width: '80%',
    alignItems: 'center',
  },
  buttonText: {
    color: '#fff',
    fontSize: 16,
  },
  icon: {
    position: 'absolute',
    top: 40,
    right: 20,
    width: 50,
    height: 50,
  },
  camera: {
    flex: 1,
    width: '100%',
  },
  buttonContainer: {
    flex: 1,
    backgroundColor: 'transparent',
    flexDirection: 'row',
    margin: 20,
  },
  text: {
    fontSize: 18,
    color: 'white',
  },
  message: {
    fontSize: 18,
    textAlign: 'center',
    margin: 10,
  },
});

export default styles;