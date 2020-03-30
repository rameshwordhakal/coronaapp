// The Cloud Functions for Firebase SDK to create Cloud Functions and setup triggers.
const functions = require('firebase-functions');

// The Firebase Admin SDK to access the Firebase Realtime Database.
const admin = require('firebase-admin');
admin.initializeApp(functions.config().firebase);

exports.dialogflowFirebaseFulfillment = functions.https.onRequest((request, response) => {
    console.log('Request headers: ' + JSON.stringify(request.headers));
    console.log('Request body: ' + JSON.stringify(request.body));

    // An action is a string used to identify what needs to be done in fulfillment
    let action = request.body.result.action; // https://dialogflow.com/docs/actions-and-parameters
    console.log('Actions = ' + JSON.stringify(action));

    let query = request.body.result.resolvedQuery;

    // Parameters are any entites that Dialogflow has extracted from the request.
    const parameters = request.body.result.parameters; // https://dialogflow.com/docs/actions-and-parameters

    // Contexts are objects used to track and store conversation state
    const inputContexts = request.body.result.contexts; // https://dialogflow.com/docs/contexts

    if (action === 'firebase.update') {
        let userId = 'bert.macklin';
        // Check if the user is in our DB
        admin.firestore().collection('users').where('userId', '==', userId).limit(1).get()
            .then(snapshot => {
                let user = snapshot.docs[0]
                if (!user) {
                    // Add the user to DB
                    admin.firestore().collection('users').add({
                        userId: userId
                    }).then(ref => {
                        sendResponse('Added new user');
                    });
                } else {
                    // User in DB
                    sendResponse('User already exists');
                }
            });
    }

    // Function to send correctly formatted responses to Dialogflow which are then sent to the user
    function sendResponse(responseToUser) {
        // if the response is a string send it as a response to the user
        if (typeof responseToUser === 'string') {
            let responseJson = {};
            responseJson.speech = responseToUser; // spoken response
            responseJson.displayText = responseToUser; // displayed response
            response.json(responseJson); // Send response to Dialogflow
        } else {
            // If the response to the user includes rich responses or contexts send them to Dialogflow
            let responseJson = {};

            // If speech or displayText is defined, use it to respond (if one isn't defined use the other's value)
            responseJson.speech = responseToUser.speech || responseToUser.displayText;
            responseJson.displayText = responseToUser.displayText || responseToUser.speech;

            // Optional: add rich messages for integrations (https://dialogflow.com/docs/rich-messages)
            responseJson.data = responseToUser.richResponses;

            // Optional: add contexts (https://dialogflow.com/docs/contexts)
            responseJson.contextOut = responseToUser.outputContexts;

            response.json(responseJson); // Send response to Dialogflow
        }
    }
});


let preformatted_html = ` <pre>
                <b>Total Cases: </b> ` + output["total_cases"]+ `
                <b>New Cases: </b> ` + output["new_cases"] +`
                <b>Total Deaths: </b> ` + output["total_deaths"] +`
                <b>New Deaths: </b> ` + output["new_deaths"] +`
                <b>Recovered: </b> ` + output["total_recovered"] +`
                <b>Active: </b>` + output["active_cases"] +`
                <b>Critical: </b> ` + output["serious_cases"] +`
                </pre>`;