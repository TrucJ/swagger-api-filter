// /static/js/filter-handler.js

import { appState } from './scripts.js';

export function handleFilterFileChange(event) {
    const file = event.target.files[0];
    const reader = new FileReader();
    
    reader.onload = function(event) {
        try {
            appState.filterData = JSON.parse(event.target.result);
        } catch (error) {
            alert('Invalid Filter JSON format');
            return;
        }

        if (appState.filterData.paths) {
            autoCheckPaths(appState.filterData.paths);
        } else {
            alert('No paths found in the Filter file.');
        }
        document.getElementById('download-filter').disabled = false;
    };

    if (file) {
        reader.readAsText(file);
    }
}

export function autoCheckPaths(filterPaths) {
    for (const path in filterPaths) {
        if (filterPaths.hasOwnProperty(path)) {
            const methods = filterPaths[path];
            for (const method of methods) {
                const checkboxId = `${method}-${path}`;
                const checkbox = document.getElementById(checkboxId);
                if (checkbox) {
                    checkbox.checked = true;
                }
            }
        }
    }
}
