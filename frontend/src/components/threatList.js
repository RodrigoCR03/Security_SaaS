import React, { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { fetchThreats } from '../actions/threatActions';
import { List } from 'antd';

function ThreatList() {
  const dispatch = useDispatch();
  const threats = useSelector(state => state.threats.items);

  useEffect(() => {
    dispatch(fetchThreats());
  }, [dispatch]);

  return (
    <List
      itemLayout="horizontal"
      dataSource={threats}
      renderItem={threat => (
        <List.Item>
          <List.Item.Meta
            title={threat.type}
            description={`${threat.description} - ${new Date(threat.timestamp).toLocaleString()}`}
          />
        </List.Item>
      )}
    />
  );
}

export default ThreatList;
