export default function divideFunction(numerator, denominator) {
    return new Promise((resolve) => {
        try {
            resolve(numerator/denominator)
        }
        catch {
            throw new Error('cannot divide by 0');
        }
    });
}