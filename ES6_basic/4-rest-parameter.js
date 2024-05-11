/* eslint-disable */
export default function returnHowManyArguments(...number_of_args) {
    let total = 0;
    for(const i in number_of_args) {
        total += i.length
    }
    return total
}