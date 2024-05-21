export default function signUpUser(firstName, lastName) {
  return new Promise((resolved) => {
    const success = true;
    if (success) {
      resolved({ firstName, lastName });
    }
  });
}
