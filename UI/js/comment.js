"use strict"
//Class that handles forms on click of buttons
class FormHandler {
    constructor(url, fieldNames) {
        this.data = {};
        this.url = url;
        this.fieldNames = fieldNames;
    }
    //gets url
    get getUrl() {
        return this.url;
    }
    //creates the object to be posted
    createFormData() {
        for (let name of this.fieldNames) {
            this.data[name] = this.getFieldValue(name);
        }
    }
    //gets the data being posted
    get Data() {
        this.createFormData()
        return JSON.stringify(this.data);
    }
    getFieldValue(name) {
        return document.getElementById(name).value;
    }
}
let commentUrl = '';