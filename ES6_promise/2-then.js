export default function handleResponseFromAPI(promise) {
    // const promise = new Promise((resolve, reject) => {
    //     if (promise) {
    //         resolve({status:200, body:"success"})
    //     }
    //     else {
    //         reject(new Error([]))
    //     }
    // })
    // // const result = 
    promise
    .then(promise => {
        console.log("Got a response from the API");
    })
}