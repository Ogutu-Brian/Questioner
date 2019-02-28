//tests for the creation of meetup
"use strict"
import puppeteer from "puppeteer";
import faker from "faker";
import {
    pageUrls
} from '../UI/js/urls.js';
const meetupForm = pageUrls.createMeetupPage;
const loginApp = pageUrls.loginPage;
const leadData = {
    email: "admin@gmail.com",
    password: 'password12#B',
    location: faker.lorem.word(),
    topic: faker.commerce.productName(),
    happeningOn: '24-08-2019',
    body: faker.lorem.text()
}
let page;
let browser;
const width = 1920;
const height = 1080;
beforeAll(async () => {
    browser = await puppeteer.launch({
        headless: true
    });
    page = await browser.newPage();
    await page.setViewport({
        width,
        height
    });
});
afterAll(() => {
    browser.close();
});
describe("Login as an admin and create meetup", () => {
    test("An admin should be able to create meetup", async () => {
        await page.goto(meetupForm);
        await page.waitForSelector('#meetup-form');
        await page.click('input[id=location]');
        await page.type('input[id=location]', leadData.location);
        await page.click('input[id=topic]');
        await page.type('input[id=topic]', leadData.topic);
        await page.click('input[id=happeningOn]');
        await page.type('input[id=happeningOn]', leadData.happeningOn);
        await page.click('textarea[id=body]');
        await page.type('textarea[id=body]', leadData.body);
        await page.click('button[id=postMeeup]');
    }, 160000);
});