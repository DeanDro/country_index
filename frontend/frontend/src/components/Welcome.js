import React from 'react';

function Welcome(props){
    return (
        <div className='introduction'>
            <div className='container'>
                <h2>Country Indexing Application</h2>
                <br></br>
                <p><b>Instructions:</b>Select the top 10 categories you consider most important to view 
                a ranking of each country based on how they perform in these areas. The information are collected 
                by publicly available sources and analysed based on your priorities list.</p>
            </div>
        </div>
    );
}

export default Welcome;