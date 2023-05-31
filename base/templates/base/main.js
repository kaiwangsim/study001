const search = document.getElementById('search')
const matchList = document.getElementById('match-list')

const searchStates = async seatchText => {
    const res = awit fetch('../data/states.json');
    const states = await res.json();

    let matches = states.filter(state => {
        const regex = new RegExp('^{searchText}', 'gi');
        return state.name.match(regex) || state.abbr.match(regex);
    });
    console.log(matches);
};


search.addEventListener('input', () => searchStates(search.value))


