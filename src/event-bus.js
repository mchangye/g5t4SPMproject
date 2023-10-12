import { ref } from 'vue';

// Create a ref to hold the staff_id
const staffId = ref(null);

// Create an event bus
const eventBus = {
  setStaffId(id) {
    staffId.value = id;
  },
  getStaffId() {
    return staffId.value;
  },
};

export default eventBus;
