import fetch from 'node-fetch';

const createProjectIfNotExists = async function () {
    const CI_PROJECT_NAME = process.env.CI_PROJECT_NAME;
    const LIGHTHOUSE_USER = process.env.LIGHTHOUSE_USER;
    const LIGHTHOUSE_PASS = process.env.LIGHTHOUSE_PASS;
    const auth_str = Buffer.from(`${LIGHTHOUSE_USER}:${LIGHTHOUSE_PASS}`).toString('base64');

    const response = await fetch(`https://lighthouse.sbdev.sk/v1/projects/slug:${CI_PROJECT_NAME}`, {
        method: 'GET',
        headers: {'Authorization': 'Basic ' + auth_str}
    });
    if (!response.ok) {
        const data = {
            "name": CI_PROJECT_NAME,
            "externalUrl": "https://github.com/github/docs",
            "baseBranch": "main"
        }
        const response = await fetch(`https://lighthouse.sbdev.sk/v1/projects`, {
            method: 'POST',
            headers: {'Authorization': 'Basic ' + auth_str, 'Content-Type': 'application/json'}, body: JSON.stringify(data),
        });
        if (response.ok) {
            const received_data = await response.json();
            const adminToken = received_data['adminToken']
            const token = received_data['token']
            console.log("Save these variables to Settings > CI/CD > variables")
            console.log(`LH_ADMIN_TOKEN: ${adminToken}`)
            console.log(`LH_TOKEN: ${token}`)
        } else {
            const received_data = await response.text();
            console.log(`ERROR: ${response.status} ${received_data}`)
        }

    }
}


const sendMetricToPlanner = async function (data_to_send) {
    const auth_str = 'fHpdnmZ4hK1QZwo0n0k4OLj4KGInYoMLGJ5w';
    const CI_PROJECT_NAME = process.env.CI_PROJECT_NAME;
    const data = {
        "project_name": CI_PROJECT_NAME,
        "name": "lighthouse",
        "type": "lighthouse",
        "data": data_to_send,
    }
    const response = await fetch(`https://planner.smartbase.sk/heartbeat`, {
        method: 'POST',
        headers: {'Authorization': 'Bearer ' + auth_str, 'Content-Type': 'application/json'}, body: JSON.stringify(data),
    });
    if (!response.ok) {
        const data = await response.text();
        console.log(data)
    }
}

if (process.argv[2] === "createProjectIfNotExists") {
    createProjectIfNotExists();
} else if (process.argv[2] === "sendMetricToPlanner") {
    sendMetricToPlanner(process.argv[3]);
} else {
    console.error("Invalid command. Usage: node create-lh-project.mjs createProjectIfNotExists|sendMetricToPlanner");
    process.exit(1);
}
