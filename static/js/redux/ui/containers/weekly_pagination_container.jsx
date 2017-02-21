import { connect } from 'react-redux';
import { WeeklyPagination } from '../weekly_pagination.jsx';
import { fetchCourseInfo } from '../../actions/modal_actions.jsx'
import { addOrRemoveCourse } from '../../actions/timetable_actions.jsx'

const mapStateToProps = (state) => {
	return {
		activeWeek: state.weeklyCalendar.activeWeek,
    	activeWeekOffset: state.weeklyCalendar.activeWeekOffset
	}
}

const mapDispatchToProps = (dispatch) => {
	return {
		setActive: (date, weekOffset) => {
			dispatch({type: "SET_ACTIVE_WEEK", date, weekOffset});
		},
		setTodayActive: () => {
			dispatch({type: "SET_TODAY_ACTIVE"});
		},
	}
}

const WeeklyPaginationContainer = connect(
	mapStateToProps,
	mapDispatchToProps
)(WeeklyPagination);

export default WeeklyPaginationContainer;