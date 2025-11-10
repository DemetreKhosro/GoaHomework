// https://www.codewars.com/kata/563089b9b7be03472d00002b/train/javascript
// Remove All The Marked Elements of a List

Array.prototype.remove_ = function (integer_list, values_list) {
    let result = [];

    for (let i = 0; i < integer_list.length; i++) {
        let element = integer_list[i];
        let isValue = false;

        for (let value of values_list) {
            if (value === element) {
                isValue = true;
            }
        }

        if (!isValue) {
            result.push(element);
        }
    }

    return result;
};
