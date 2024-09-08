// Configure DataTable
$(document).ready(function() {
    var table = $('#restaurantTable').DataTable({
        // Configure column definitions
        "columnDefs": [
            { "searchable": false, "targets": 6 }  // Disable search in the "Actions" column
        ],
        // Configure the language settings for the DataTable
        language: {
            search: 'Cerca:',
            entries: {
                _: 'entrades',
                1: 'entrada'
            }
        },
        // Set the initial order of the columns
        order: [[0, 'asc'], [2, 'asc']],
        // Configure the layout of the DataTable
        layout: {
            topStart: {
                pageLength: {
                    menu: [5, 10, 25, 50]
                }
            },
            topEnd: {
                search: {
                    processing: true
                }
            },
            bottomStart: {
                info: {
                    info: 'Showing page _PAGE_ of _PAGES_',
                    text: 'Es mostren _START_ a _END_ _ENTRIES-TOTAL_',
                    empty: 'No hi ha entrades per mostrar',
                    search: ' (filtrat de _MAX_ entrades)'
                }
            },
            bottomEnd: {
                paging: {
                    numbers: true  // Enable pagination with numbers
                }
            }
        }
    });
});