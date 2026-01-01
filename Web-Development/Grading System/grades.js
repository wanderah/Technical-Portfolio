// grades.js

// Task 2.f: Add the test data provided in Table 1
let studentRecords = [
    { name: "Abol", grade: 74 },
    { name: "Bearl", grade: 46 },
    { name: "Ziml", grade: 88 }
];

let currentSortOrder = 'none'; // Tracks current sort state

// --- Core Functionality ---

// Function to calculate and display the average grade
function calculateAverage() {
    if (studentRecords.length === 0) {
        $("#averageGrade").text("--");
        return;
    }
    const sum = studentRecords.reduce((total, record) => total + record.grade, 0);
    const average = sum / studentRecords.length;
    // Display average, rounded to 2 decimal places
    document.getElementById('averageGrade').textContent = average.toFixed(2);
}

// Function to render the HTML table from the studentRecords array
// Task 2.b: Dynamically displays the data in an HTML table
// Task 2.d: Highlight grades above 60 in green
function renderTable() {
    const tbody = document.getElementById('gradesTableBody');
    tbody.innerHTML = ''; // Clear existing rows

    studentRecords.forEach((record, index) => {
        const row = tbody.insertRow();
        
        // 1. Delete Button Column (Task 2.e)
        const deleteCell = row.insertCell();
        deleteCell.innerHTML = `<button class="delete-btn" data-index="${index}">Delete</button>`;
        
        // 2. Name Column
        row.insertCell().textContent = record.name;
        
        // 3. Grade Column (Task 2.d: Highlighting)
        const gradeCell = row.insertCell();
        gradeCell.textContent = record.grade;
        
        // Highlight grades above 60
        if (record.grade > 60) {
            gradeCell.classList.add('highlight');
        }
    });

    calculateAverage();
}

// Function to handle adding a new student
// Task 2.a: Add student name and grade (0-100)
// Task 2.b: Add to array and update table
function addStudent(e) {
    e.preventDefault();
    
    const nameInput = document.getElementById('studentName');
    const gradeInput = document.getElementById('studentGrade');
    
    const name = nameInput.value.trim();
    const grade = parseInt(gradeInput.value);
    
    // Simple client-side validation
    if (name === "" || isNaN(grade) || grade < 0 || grade > 100) {
        alert("Please enter a valid student name and a grade between 0 and 100.");
        return;
    }

    // Add to array
    studentRecords.push({ name: name, grade: grade });
    
    // Update the display
    renderTable();
    
    // Clear form
    nameInput.value = '';
    gradeInput.value = '';
}

// Function to handle sorting
// Task 2.c: Sort the table by grade in ascending or descending
function sortTable(sortOrder) {
    if (sortOrder === 'none') {
        // To restore the original order (if possible, by name or initial index)
        // Since we don't track original index, we'll sort by name as a fallback for 'none'
        studentRecords.sort((a, b) => a.name.localeCompare(b.name));
    } else if (sortOrder === 'asc') {
        // Ascending sort (low grade to high grade)
        studentRecords.sort((a, b) => a.grade - b.grade);
    } else if (sortOrder === 'desc') {
        // Descending sort (high grade to low grade)
        studentRecords.sort((a, b) => b.grade - a.grade);
    }
    
    // After sorting the array, re-render the table
    renderTable();
}

// Function to handle deleting a record
// Task 2.e: Delete a specific student record
function deleteRecord(index) {
    // Remove one element starting at the given index
    studentRecords.splice(index, 1);
    
    // Re-render the table to reflect the change
    renderTable();
}

// --- Event Listeners and Initialization ---

document.addEventListener('DOMContentLoaded', () => {
    // Initial load of the table with test data
    renderTable(); 
    
    // Event listener for adding a new student
    document.getElementById('addStudentForm').addEventListener('submit', addStudent);

    // Event listener for sorting control
    document.getElementById('sortOrder').addEventListener('change', function() {
        sortTable(this.value);
    });

    // Event delegation for delete buttons (Task 2.e)
    document.getElementById('gradesTableBody').addEventListener('click', function(e) {
        if (e.target.classList.contains('delete-btn')) {
            // The data-index attribute holds the current index in the array
            const indexToDelete = parseInt(e.target.dataset.index);
            deleteRecord(indexToDelete);
        }
    });
});