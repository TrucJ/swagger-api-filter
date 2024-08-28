// /static/js/filter-handler.js

import { changeStatusFilterData, getStatusFilterData } from './form-handler.js';

export function handleFilterFileChange(event) {
    const file = event.target.files[0];
    const reader = new FileReader();
    
    reader.onload = function(event) {
        try {
            const filterData = JSON.parse(event.target.result);
            if (filterData.paths) {
                for (const path in filterData.paths) {
                    if (filterData.paths.hasOwnProperty(path)) {
                        const methods = filterData.paths[path];
                        for (const method of methods) {
                            const checkboxId = `${method}-${path}`;
                            if (!getStatusFilterData(checkboxId)) {
                                changeStatusFilterData(checkboxId);
                            }
                        }
                    }
                }
            } else {
                alert('No paths found in the Filter file.');
            }
        } catch (error) {
            alert('Invalid Filter JSON format');
            return;
        }
    };

    if (file) {
        reader.readAsText(file);
    }
}
