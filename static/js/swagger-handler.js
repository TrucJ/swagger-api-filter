// /static/js/swagger-handler.js

import { changeStatusFilterData } from './form-handler.js';
import { methodColorMap } from './global.js';

export function handleSwaggerFileChange(event) {
    const file = event.target.files[0];
    const reader = new FileReader(); 

    reader.onload = function(event) {
        const swaggerContent = event.target.result;
        let swaggerJson;

        try {
            swaggerJson = JSON.parse(swaggerContent);
        } catch (error) {
            alert('Invalid Swagger JSON format');
            return;
        }

        const paths = swaggerJson.paths || {};
        const pathsListElement = document.getElementById('paths-list');
        pathsListElement.innerHTML = ''; // Clear previous content

        for (const path in paths) {
            if (paths.hasOwnProperty(path)) {
                const methods = paths[path];
                for (const method in methods) {
                    if (methods.hasOwnProperty(method)) {
                        const pathItem = document.createElement('div');
                        pathItem.className = `form-check`;
                        pathItem.id = `${method}-${path}`;
                        pathItem.style.borderStyle = 'solid';
                        pathItem.style.borderWidth = '2px';
                        pathItem.style.borderColor = methodColorMap[method.toUpperCase()];
                        pathItem.style.color = methodColorMap[method.toUpperCase()];
                        pathItem.textContent = `${method.toUpperCase()} ${path}`;

                        pathItem.addEventListener('click', event => changeStatusFilterData(event.target.id));

                        pathsListElement.appendChild(pathItem);
                    }
                }
            }
        }

        if (!pathsListElement.innerHTML) {
            pathsListElement.innerHTML = '<p>No paths found in the Swagger file.</p>';
        }

        // Enable the filter file input once Swagger file is chosen
        document.getElementById('filter').disabled = false;
    };

    if (file) {
        reader.readAsText(file);
    }
}
