import React, { useEffect, useState } from 'react';
import { getPrivacySettings, updatePrivacySettings } from '../services/api';
import { Form, Switch, Button, message } from 'antd';

function PrivacyPanel() {
  const [settings, setSettings] = useState({});

  useEffect(() => {
    getPrivacySettings().then(response => {
      setSettings(response.data.settings);
    });
  }, []);

  const onFinish = values => {
    updatePrivacySettings(values).then(() => {
      message.success('Configurações atualizadas com sucesso');
    });
  };

  return (
    <Form initialValues={settings} onFinish={onFinish}>
      <Form.Item name="tracking_cookies" label="Bloquear Cookies de Rastreamento" valuePropName="checked">
        <Switch />
      </Form.Item>
      <Form.Item name="history_cleanup" label="Limpar Histórico de Navegação" valuePropName="checked">
        <Switch />
      </Form.Item>
      <Form.Item name="data_monitoring" label="Monitorizar Dados Pessoais" valuePropName="checked">
        <Switch />
      </Form.Item>
      <Button type="primary" htmlType="submit">Salvar Configurações</Button>
    </Form>
  );
}

export default PrivacyPanel;
