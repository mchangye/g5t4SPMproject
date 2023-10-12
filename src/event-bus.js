import { reactive } from 'vue';

const EventBus = reactive({
  staffId: null, // Initialize staffId to null

  // Method to set staffId and store it in localStorage
  setStaffId(staffId) {
    this.staffId = staffId;
    localStorage.setItem('staff_id', staffId);
  },

  // Method to get staffId from localStorage
  getStaffId() {
    if (!this.staffId) {
      // If staffId is not in memory, retrieve it from localStorage
      const storedStaffId = localStorage.getItem('staff_id');
      if (storedStaffId) {
        this.staffId = storedStaffId;
      }
    }
    return this.staffId;
  },


});

export default EventBus;
