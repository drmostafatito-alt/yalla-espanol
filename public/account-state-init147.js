/* Account boot phase1: restore local state before teaching scripts can save it. */
load();
applyCourse(state.activeCourseId||'main');
/* Later-level sessions stay pending until the account access check loads their catalogue. */
