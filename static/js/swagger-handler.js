// /static/js/swagger-handler.js

import { appState } from './scripts.js';
import { updateFilterData } from './form-handler.js';
import { autoCheckPaths } from './filter-handler.js';

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
                        pathItem.className = "form-check";

                        const checkbox = document.createElement('input');
                        checkbox.type = 'checkbox';
                        checkbox.className = 'form-check-input';
                        checkbox.id = `${method}-${path}`;
                        checkbox.name = 'api-paths';
                        checkbox.value = `${method.toUpperCase()} ${path}`;

                        const label = document.createElement('label');
                        label.className = 'form-check-label';
                        label.htmlFor = checkbox.id;
                        label.innerHTML = `<strong>${method.toUpperCase()}</strong> ${path}`;

                        checkbox.addEventListener('change', updateFilterData);

                        pathItem.appendChild(checkbox);
                        pathItem.appendChild(label);
                        pathsListElement.appendChild(pathItem);
                    }
                }
            }
        }

        if (!pathsListElement.innerHTML) {
            pathsListElement.innerHTML = '<p>No paths found in the Swagger file.</p>';
        }

        if (appState.filterData && appState.filterData.paths) {
            autoCheckPaths(appState.filterData.paths);
        }
    };

    if (file) {
        reader.readAsText(file);
    }
}
