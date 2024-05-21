export default function signUpUser(firstName, lastName) {
    return new Promise((resolved) => {
        let success = true
        if (success) {
            resolved({firstName, lastName})
        }
    });
}